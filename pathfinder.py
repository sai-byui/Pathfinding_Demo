import math


class Pathfinder:
    def __init__(self, node_list, start_node, finish_node):
        self.open_list = []
        self.closed_list = []
        self.final_path_list = []
        self.unvisited = node_list
        self.start_node = start_node
        self.finish_node = finish_node
        self.current_node = None

    def distance(self, node1, node2):
        return math.sqrt((node1.sprite.rect.x - node2.sprite.rect.x)**2 +
                         (node1.sprite.rect.y - node2.sprite.rect.y)**2)

    def get_g_cost(self, node):
        return self.distance(self.current_node, node) + self.current_node.g_cost

    def get_h_cost(self, node):
        return self.distance(node, self.finish_node)

    def get_f_cost(self, node):
        return node.g_cost + node.h_cost

    def print_path(self, node):
        for n in node.path_to_me:
            print(str(n.sprite.rect.x) + ", " + str(n.sprite.rect.y))

    def add_to_open(self, node):
        if not self.open_list:
            self.open_list.append(node)
            return

        i = 0
        inserted = False
        for current_node in self.open_list:
            if (node.f_cost*1.0 + node.h_cost*0.0) * 0.5 < (current_node.f_cost*1.0 + current_node.h_cost*0.0) * 0.5:
                self.open_list.insert(i, node)
                inserted = True
                break
            else:
                i += 1

        if not inserted:
            self.open_list.append(node)

    def take_step(self):
        if self.finish_node in self.closed_list:
            self.final_path_list = self.finish_node.path_to_me
            for node in self.final_path_list:
                node.update_bg(0x0000ff)
        elif self.start_node in self.unvisited:
            self.start_node.g_cost = 0
            self.start_node.h_cost = self.get_h_cost(self.start_node)
            self.start_node.f_cost = self.get_f_cost(self.start_node)
            self.unvisited.remove(self.start_node)
            self.add_to_open(self.start_node)
            self.start_node.update_bg(0x00ff00)
        elif self.open_list:
            self.current_node = self.open_list[0]
            found_node = False
            for node in self.current_node.connections:
                if not node.is_blocking and self.current_node not in node.path_to_me:
                    if node in self.unvisited:
                        node.set_g_cost(self.get_g_cost(node))
                        node.set_h_cost(self.get_h_cost(node))
                        node.set_f_cost(self.get_f_cost(node))
                        node.path_to_me = self.current_node.path_to_me + [self.current_node]
                        self.unvisited.remove(node)
                        self.add_to_open(node)
                        node.update_bg(0x00ff00)
                        found_node = True
                        break
                    elif node in self.open_list:
                        temp_g = self.get_g_cost(node)
                        temp_h = self.get_h_cost(node)
                        temp_f = temp_g + temp_h
                        if temp_f < node.f_cost:
                            node.set_g_cost(temp_g)
                            node.set_h_cost(temp_h)
                            node.set_f_cost(temp_f)
                            node.update_bg(0x00ff00)
                            self.open_list.remove(node)  # make sure it stays sorted
                            self.add_to_open(node)
                            node.path_to_me = self.current_node.path_to_me + [self.current_node]
                            found_node = True
                            break
            if not found_node:
                self.open_list.remove(self.current_node)
                self.closed_list += [self.current_node]
                self.current_node.update_bg(0xff0000)







