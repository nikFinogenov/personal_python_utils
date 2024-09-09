class Tree:
    seed: str
    fertilizer: bool
    water: int

    def getTreeInfo(self):
        print("Seed: " + self.seed + ", fertilizer: " + str(self.fertilizer) + ", water(L): " + str(self.water))


class GardenMan:
    def growUpTree(self):
        pass

    def setSeed(self, seed: str):
        pass

    def setFertilizer(self, fertilizer: bool):
        pass

    def setWater(self, water: int):
        pass

    def getResult(self):
        pass


class TreeBuilder (GardenMan):
    tree: Tree

    def growUpTree(self):
        self.tree = Tree()

    def setSeed(self, seed):
        self.tree.seed = seed

    def setFertilizer(self, fertilizer):
        self.tree.fertilizer = fertilizer

    def setWater(self, water):
        self.tree.water = water

    def getResult(self):
        return self.tree


if __name__ == "__main__":
    builder = TreeBuilder()
    builder.growUpTree()
    builder.setSeed("orange")
    builder.setFertilizer(True)
    builder.setWater(10)
    tree = builder.getResult()
    tree.getTreeInfo()