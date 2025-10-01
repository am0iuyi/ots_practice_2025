import turtle


def perform_switch_case(state, t, turn):
    x = round(t.position()[0] / 10)
    y = round(t.position()[1] / 10)
    num_turns = 5

    if state == "right":
        t.forward(10)  # Перемещение

        if x >= turn:
            state = "down"
            t.setheading(270)  #  Разворот вниз
            return state, turn
        return state, turn
    if state == "stop":

        return state, turn
    if state == "down":
        t.forward(10)  # Перемещение

        if y <= -turn:
            state = "left"
            t.setheading(180)  #  Разворот влево
            turn = turn + 1  #  Начало нового витка
            return state, turn
        return state, turn
    if state == "init":

        if True:
            state = "right"
            return state, turn
        return state, turn
    return state, turn


def draw():
    start_state = "stop"
    end_state = "left"
    curr_state = start_state
    t = turtle.Turtle()
    t.speed(0)
    turn = 1

    while curr_state != end_state:
        curr_state, turn = perform_switch_case(curr_state, t, turn)
    turtle.done()


if  __name__ == "__main__":
    draw()