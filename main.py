def on_gesture_shake():
    basic.show_icon(IconNames.SURPRISED)
    basic.pause(1000)
    basic.show_icon(IconNames.HAPPY)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

basic.show_icon(IconNames.HAPPY)