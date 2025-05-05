toggle := false

F3::
toggle := !toggle
if (toggle) {
    SetTimer, PressE, 10  ; Adjust the interval (ms) as needed
} else {
    SetTimer, PressE, Off
}
return

PressE:
Send, r
return
