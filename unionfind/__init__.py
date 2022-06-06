from typing import Dict, Iterable
from enum import Enum


class UnionMethod(Enum):
    BY_RANK = 0,
    BY_SIZE = 1


class DisjointSetUnion:
    """
    Reference: https://cp-algorithms.com/data_structures/disjoint_set_union.html

    Time complexities for a disjoint set initialized with n elements where m can be either union or find operation:
    - Raw unoptimized => O(n) per operation, O(mn) for m operations
    - With union-by-rank/size but without path compression => O(log(n)) per operation, O(m·log(n)) for m operations
    - With union-by-rank/size and path compression => O(⍺(n)) per operation, O(m·⍺(n)) for m operations
        Here ⍺(n) is inverse Ackermann function which grows very slowly, so ⍺(n) as a whole caps out at 4. So
        asymptotically, it only takes O(m) time for m operations or O(1) per operation.

    This is a full implementation of DisjointSetUnion capable of performing both, union-by-rank or union-by-size.
    You'll need to pass the union method at the time of creating an instance of DisjointSetUnion (defaults to union-by-rank)

    NOTE: For graph applications, DisjointSetUnion data structure _only_ works with undirected graphs
    """
    def __init__(self, union_method: UnionMethod = UnionMethod.BY_RANK):
        self._disjoint_set_count = 0
        self._largest_disjoint_set_size = 0  # only computed if performing union-by-size
        self._union_method = union_method
        self._representatives: Dict[str, str] = {}
        # use one from rank/size for your implementation; both are added here as this is an illustrative data structure
        self._ranks: Dict[str, int] = {}
        self._sizes: Dict[str, int] = {}

    def make_set(self, elements: Iterable[str]) -> None:
        element_added = False
        for e in elements:
            if e not in self._representatives:
                element_added = True
                self._representatives[e] = e
                self._ranks[e] = 0
                self._sizes[e] = 1
                self._disjoint_set_count += 1
        if element_added:
            self._largest_disjoint_set_size = max(self._largest_disjoint_set_size, 1)

    def find_set(self, element: str) -> str:
        if self._representatives[element] != element:
            # compress path while finding the top-level representative
            self._representatives[element] = self.find_set(self._representatives[element])
        return self._representatives[element]
    
    def union_set(self, element1: str, element2: str) -> bool:
        rep1 = self.find_set(element1)
        rep2 = self.find_set(element2)

        # elements are in the same set and have a common group representative
        if rep1 == rep2:
            return False  # union not performed

        if self._union_method == UnionMethod.BY_RANK:
            self._union_by_rank(rep1, rep2)
        else:
            self._union_by_size(rep1, rep2)

        # total disjoint set count reduced by one after the union
        self._disjoint_set_count -= 1
        
        # union performed
        return True

    def _union_by_rank(self, rep1: str, rep2: str) -> None:
        if self._ranks[rep1] < self._ranks[rep2]:
            rep1, rep2 = rep2, rep1
        self._representatives[rep2] = rep1
        self._ranks[rep1] += 1

    def _union_by_size(self, rep1: str, rep2: str) -> None:
        if self._sizes[rep1] < self._sizes[rep2]:
            rep1, rep2 = rep2, rep1
        self._representatives[rep2] = rep1
        self._sizes[rep1] += self._sizes[rep2]
        self._largest_disjoint_set_size = max(self._largest_disjoint_set_size, self._sizes[rep1])

    def get_union_method(self) -> UnionMethod:
        """
        Returns the union method being used by the data structure
        """
        return self._union_method

    def get_representatives(self) -> Dict[str, str]:
        """
        Get representatives of all elements in the data structure at the moment
        """
        return {e: self.find_set(e) for e in self._representatives.keys()}

    def get_disjoint_set_count(self) -> int:
        """
        Get total number of disjoint sets in the data structure at the moment
        """
        return self._disjoint_set_count

    def get_largest_disjoint_set_size(self) -> int:
        """
        Get size of the largest disjoint set that exists in the data structure thus far...
        Only works if performing union-by-size (union_method=UnionMethod.BY_SIZE)
        Very useful in solving problems like finding the size of the longest consecutive sequence in an array
        """
        return self._largest_disjoint_set_size

    def __str__(self):
        return "DisjointSetUnion@{}: {}\n-> Representatives: {}\n-> Total disjoint set count: {}\n-> Size of the largest disjoint set: {}".format(
            id(self),
            self.get_union_method(),
            list(self.get_representatives().values()),
            self.get_disjoint_set_count(),
            self.get_largest_disjoint_set_size()
        )


if __name__ == '__main__':
    dsu = DisjointSetUnion(union_method=UnionMethod.BY_SIZE)
    print(dsu)

    print("\nPerforming make_set {'A', 'B', 'C', 'D', 'E'}")
    dsu.make_set(['A', 'B', 'C', 'D', 'E'])
    print(dsu)

    print("\nPerforming union_set {'D', 'C'}")
    dsu.union_set('D', 'C')
    print(dsu)

    print("\nPerforming union_set {'B', 'A'}")
    dsu.union_set('B', 'A')
    print(dsu)

    print("\nPerforming union_set {'A', 'C'}")
    dsu.union_set('A', 'C')
    print(dsu)

    print("\nPerforming union_set {'D', 'E'}")
    dsu.union_set('D', 'E')
    print(dsu)

    print("\nPerforming make_set {'F', 'G', 'H'}")
    dsu.make_set(['F', 'G', 'H'])
    print(dsu)

    print("\nPerforming union_set {'F', 'G'}")
    dsu.union_set('F', 'G')
    print(dsu)

    print("\nPerforming union_set {'F', 'A'}")
    dsu.union_set('F', 'A')
    print(dsu)
