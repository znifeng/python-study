#!/usr/bin/python
# -*- coding: utf-8 -*
import random

alpha = 0.2
gamma = 0.8
epsilon = 0.8
iteration =10
reward_matrix = [
    [0, 4, 2, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 5, 3, 0],
    [0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
]
q_matrix = [
    [-1, 0, 0, -1, -1, -1],
    [-1, -1, -1, 0, -1, -1],
    [-1, -1, -1, 0, 0, -1],
    [-1, -1, -1, -1, -1, 0],
    [-1, -1, -1, -1, -1, 0],
    [-1, -1, -1, -1, -1, -1],
]

class ReforcementLearningDemo:
    def __init__(self, reward_matrix, q_matrix, alpha, gamma, epsilon):
        self.reward_matrix = reward_matrix
        self.q_matrix = q_matrix
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.curret_location = 0
        self.next_location = None

    def train(self, iteration):
        for i in range(iteration):
            self._one_iteration()

    def get_next_location(self):
        q_values = self.q_matrix[self.curret_location]
        next_location_set =  [ location for location,val in enumerate(q_values) if val >= 0 ]

        if len(next_location_set) == 0:
            return None

        elif len(next_location_set) == 1:
            return next_location_set[0]

        else:
            max_reward = max(q_values)
            max_reward_location = [ location for location,val in enumerate(q_values) if val == max_reward][0]
            next_location_set.remove(max_reward_location)
            if random.random()<= epsilon:
                return max_reward_location
            else:
                return random.choice(next_location_set)

    def _one_iteration(self):
        self.next_location = self.get_next_location()
        while self.next_location != None:
            current_q = self.q_matrix[self.curret_location][self.next_location]
            reward = self.reward_matrix[self.curret_location][self.next_location]
            next_max_q = max(self.q_matrix[self.next_location])
            self.q_matrix[self.curret_location][self.next_location] += self.alpha * (reward + self.gamma * next_max_q - current_q)
            self.curret_location = self.next_location
            self.next_location = self.get_next_location()

        self.curret_location = 0

    def print_q_matrix(self):
        for item in self.q_matrix:
            print item


if __name__ == '__main__':
    demo = ReforcementLearningDemo(reward_matrix, q_matrix, alpha, gamma, epsilon)
    demo.train(10000)
    demo.print_q_matrix()