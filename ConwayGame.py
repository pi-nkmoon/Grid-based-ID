import numpy as np
import matplotlib.pyplot as plt


def evolve_generation(current_gen):
    size = current_gen.shape[0]
    new_gen = np.zeros_like(current_gen)

    for i in range(size):
        for j in range(size):
            neighbors = [
                ((i - 1) % size, (j - 1) % size),
                ((i - 1) % size, j),
                ((i - 1) % size, (j + 1) % size),
                (i, (j - 1) % size),
                (i, (j + 1) % size),
                ((i + 1) % size, (j - 1) % size),
                ((i + 1) % size, j),
                ((i + 1) % size, (j + 1) % size),
            ]
            live_neighbors = sum(current_gen[x, y] for x, y in neighbors)

            if current_gen[i, j] == 1:
                if live_neighbors == 2 or live_neighbors == 3:
                    new_gen[i, j] = 1
            else:
                if live_neighbors == 3:
                    new_gen[i, j] = 1

    return new_gen


def ShowCode(binary_matrix):
    plt.figure()
    plt.title(f'Size: {binary_matrix.shape[0]}')
    plt.imshow(binary_matrix, cmap='gray', interpolation='nearest')
    plt.show()


class ConwayVerifier:
    def __init__(self, capacity, size):
        self.size = size
        self.admin_key = np.random.choice([0, 1], size=(self.size, self.size))
        self.capacity = capacity
        self.lastGen = 0

    def UpdateAdminKey(self, key):
        self.admin_key = key

    def GenerateKey(self):
        if self.capacity == self.lastGen:
            print("Capacity Exhausted")
            return
        temp_gen = self.admin_key
        self.lastGen = self.lastGen + 1
        for _ in range(self.lastGen):
            temp_gen = evolve_generation(temp_gen)

        return np.bitwise_xor(temp_gen, self.admin_key)

    def GetAdmittedNumber(self):
        return self.lastGen

    def verify(self, key):
        temp_gen = self.admin_key
        for _ in range(self.lastGen):
            temp_gen = evolve_generation(temp_gen)
            xor_gen = np.bitwise_xor(temp_gen, self.admin_key)
            if (key == xor_gen).all():
                return True

        return False
