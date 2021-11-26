import sys
sys.stdin = open('input.txt')

def in_order(node):
    if len(graph[node]) < 3:
        return graph[node][1]
    elif len(graph[node]) == 3:
        left_node = int(graph[node][2])-1
        return in_order(left_node) + graph[node][1]
    else:
        left_node = int(graph[node][2])-1
        right_node = int(graph[node][3])-1
        return in_order(left_node) + graph[node][1] + in_order(right_node)

for T in range(10):
    N = int(input())
    graph = {i : input().split() for i in range(N)}
    print('#{} {}'.format((T+1), in_order(0)))

#1 SOFTWARE
#2 COMPUTER_SCIENCE_AND_ENGINEERING
#3 SOFWARE_ALGORITHM_AND_DATA_STRUCT
#4 DEPTH_FIRST_SEARCH_AND_BREATH_FIRST_SEARCH
#5 WELCOME_TO_ALGORITHM_PROBLEM_SOLVING
#6 ARRAY_STRING_STACK_QUEUE_TREE_GRAPH
#7 HE_WHO_WOULD_HAVE_THE_KERNEL_MUST_CRACK_THE_SHELL
#8 THE_PRESENT_IS_THE_PRESENT_MOMENT
#9 IN_ORDER_PRE_ORDER_POST_ORDER_TRACE
#10 TECHNOLOGY_TRAINING_INSTITUTE