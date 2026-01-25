import sdl3
import sdl3.SDL_image
import ctypes

#init SDL Video
sdl3.SDL_Init(sdl3.SDL_INIT_VIDEO)

#window and renderer
WIDTH = 768
HEIGHT = 360
window = sdl3.SDL_CreateWindow("Keyboard Tester".encode(),WIDTH,HEIGHT,0)
renderer = sdl3.SDL_CreateRenderer(window,None)
window_surface = sdl3.SDL_GetWindowSurface(window)

#colors
white = sdl3.SDL_MapSurfaceRGB(window_surface,255,255,255)
green = sdl3.SDL_MapSurfaceRGB(window_surface,124,255,0)
kellygreen = sdl3.SDL_MapSurfaceRGB(window_surface,76,187,23)

#main
buttons = {
    # 40x40
    "a": (WIDTH//2-253, HEIGHT//2-18, 40, 40),
    "b": (WIDTH//2-44, HEIGHT//2 + 28, 40, 40),
    "c": (WIDTH//2-141, HEIGHT//2+28, 40, 40),
    "d": (WIDTH//2-155, HEIGHT//2-18, 40, 40),
    "e": (WIDTH//2-176, HEIGHT//2-67, 40, 40),
    "f": (WIDTH//2-106, HEIGHT//2-18, 40, 40),
    "g": (WIDTH//2-57, HEIGHT//2-18, 40, 40),
    "h": (WIDTH//2-9, HEIGHT//2-18, 40, 40),
    "i": (WIDTH//2 + 67, HEIGHT//2-67, 40, 40),
    "j": (WIDTH//2+40, HEIGHT//2-18, 40, 40),
    "k": (WIDTH//2+89, HEIGHT//2-18, 40, 40),
    "l": (WIDTH//2+136, HEIGHT//2-18, 40, 40),
    "m": (WIDTH//2+53, HEIGHT//2+28, 40, 40),
    "n": (WIDTH//2+5, HEIGHT//2+28, 40, 40),
    "o": (WIDTH//2 + 116, HEIGHT//2-67, 40, 40),
    "p": (WIDTH//2 + 164, HEIGHT//2-67, 40, 40),
    "q": (WIDTH//2-274, HEIGHT//2-67, 40, 40),
    "r": (WIDTH//2-127, HEIGHT//2-67, 40, 40),
    "s": (WIDTH//2-204, HEIGHT//2-18, 40, 40),
    "t": (WIDTH//2-79, HEIGHT//2-67, 40, 40),
    "u": (WIDTH//2+18, HEIGHT//2-67, 40, 40),
    "v": (WIDTH//2-92, HEIGHT//2+28, 40, 40),
    "w": (WIDTH//2-225, HEIGHT//2-67, 40, 40),
    "x": (WIDTH//2-190, HEIGHT//2+28, 40, 40),
    "y": (WIDTH//2-30, HEIGHT//2-67, 40, 40),
    "z": (WIDTH//2-239, HEIGHT//2+28, 40, 40),
    ";": (WIDTH//2+185, HEIGHT//2-18, 40, 40),
    "'": (WIDTH//2+234, HEIGHT//2-18, 40, 40),
    "[": (WIDTH//2 + 213, HEIGHT//2-67, 40, 40),
    "]": (WIDTH//2 + 261, HEIGHT//2-67, 40, 40),
    "\\": (WIDTH//2 + 309, HEIGHT//2-67, 40, 40),
    "<": (WIDTH//2+101, HEIGHT//2+28, 40, 40),
    ">": (WIDTH//2+149, HEIGHT//2+28, 40, 40),
    "?": (WIDTH//2+198, HEIGHT//2+28, 40, 40),
    "1": (WIDTH//2-301, HEIGHT//2-113, 40, 40),
    "2": (WIDTH//2-253, HEIGHT//2-113, 40, 40),
    "3": (WIDTH//2-204, HEIGHT//2-113, 40, 40),
    "4": (WIDTH//2-156, HEIGHT//2-113, 40, 40),
    "5": (WIDTH//2-108, HEIGHT//2-113, 40, 40),
    "6": (WIDTH//2-59, HEIGHT//2-113, 40, 40),
    "7": (WIDTH//2-11, HEIGHT//2-113, 40, 40),
    "8": (WIDTH//2+37, HEIGHT//2-113, 40, 40),
    "9": (WIDTH//2+86, HEIGHT//2-113, 40, 40),
    "0": (WIDTH//2+134, HEIGHT//2-113, 40, 40),
    "`": (WIDTH//2-350, HEIGHT//2-113, 40, 40),
    "-": (WIDTH//2+183, HEIGHT//2-113, 40, 40),
    "=": (WIDTH//2+231, HEIGHT//2-113, 40, 40),
    "left ctrl": (WIDTH//2-350, HEIGHT//2+73, 40, 40),
    "windows": (WIDTH//2-301, HEIGHT//2+73, 40, 40),
    "left alt": (WIDTH//2-203, HEIGHT//2+73, 40, 40),
    "right alt": (WIDTH//2+308, HEIGHT//2+72, 40, 40),

    # 70x40
    "backspace": (WIDTH//2+279, HEIGHT//2-113, 70, 40),
    "tab": (WIDTH//2-350, HEIGHT//2-65, 70, 40),
    "enter": (WIDTH//2+280, HEIGHT//2-18, 70, 40),

    # 90x40
    "caps lock": (WIDTH//2-350, HEIGHT//2-18, 90, 40),

    # 103x40
    "left shift": (WIDTH//2-350, HEIGHT//2+28, 103, 40),
    "right shift": (WIDTH//2+246, HEIGHT//2+28, 103, 40),

    # 96x40
    "right ctrl": (WIDTH//2+205, HEIGHT//2+73, 96, 40),

    # space
    "space": (WIDTH//2-156, HEIGHT//2+73, 355, 40)
}

special ={sdl3.SDL_SCANCODE_LGUI: "windows",sdl3.SDL_SCANCODE_RETURN:"enter",sdl3.SDL_SCANCODE_CAPSLOCK:"caps lock"}



# Example
#char = ctypes.c_char_p(b"k")
#g = sdl3.SDL_GetKeyFromName(char) 
#scancode_from_g = sdl3.SDL_GetScancodeFromKey(g)
#print(g,scancode_from_g)

pressed_keys = set()

# highlight and repeated highlight functions
def highlight(key_name):
    if key_name in buttons:
        x,y,w,h = buttons[key_name]
        rect = sdl3.SDL_Rect(x,y,w,h)
        sdl3.SDL_SetSurfaceBlendMode(window_surface,sdl3.SDL_BLENDMODE_BLEND)
        sdl3.SDL_FillSurfaceRect(window_surface,rect,green)
    elif key_name in special.values():
        buttons_name = special[key_name]
        x,y,w,h = buttons[buttons_name]
        rect = sdl3.SDL_Rect(x,y,w,h)
        sdl3.SDL_SetSurfaceBlendMode(window_surface,sdl3.SDL_BLENDMODE_BLEND)
        sdl3.SDL_FillSurfaceRect(window_surface,rect,green)

def povtornyi_highlight(key_name):
    if key_name in buttons:
        x,y,w,h = buttons[key_name]
        rect = sdl3.SDL_Rect(x,y,w,h)
        sdl3.SDL_SetSurfaceBlendMode(window_surface,sdl3.SDL_BLENDMODE_BLEND)
        sdl3.SDL_FillSurfaceRect(window_surface,rect,kellygreen)
    elif key_name in special.values():
        x,y,w,h = buttons[key_name]
        rect = sdl3.SDL_Rect(x,y,w,h)
        sdl3.SDL_SetSurfaceBlendMode(window_surface,sdl3.SDL_BLENDMODE_BLEND)
        sdl3.SDL_FillSurfaceRect(window_surface,rect,kellygreen)
    
# load <image format> into surface    
image_surface = sdl3.SDL_image.IMG_Load(b"keyboard_layout.png")

if not image_surface:
    print("Failed to load PNG:", sdl3.SDL_GetError().decode())
    exit(1)   


#Event loop running (main loop)
event = sdl3.SDL_Event()
running = True
while running:
    while sdl3.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl3.SDL_EVENT_QUIT:
            running = False
    
    keyboard_state = sdl3.SDL_GetKeyboardState(None)

    sdl3.SDL_FillSurfaceRect(window_surface,None,0xFFFFFF)
    #Default keys
    for k in pressed_keys:
        highlight(k)
    
    for key_name,(x,y,w,h) in buttons.items():
        keychar = ctypes.c_char_p(key_name.encode())
        key = sdl3.SDL_GetKeyFromName(keychar)
        scancode = sdl3.SDL_GetScancodeFromKey(key,None)
        if keyboard_state[scancode]:
            print(f"User pressed '{key_name}'")
            highlight(key_name)
            pressed_keys.add(key_name)
        if keyboard_state[scancode] and key_name in pressed_keys:
            povtornyi_highlight(key_name)
    #Special keys
    for key,name in special.items():
        if keyboard_state[key]:
            print(f"User pressed '{name}'")
            highlight(name)
            pressed_keys.add(name)
        if keyboard_state[key] and name in pressed_keys:
            povtornyi_highlight(name)


    sdl3.SDL_BlitSurface(image_surface, None, window_surface, None) 
    sdl3.SDL_UpdateWindowSurface(window)

# Cleanup
sdl3.SDL_DestroyWindow(window)
sdl3.SDL_Quit()
#P.S: fn doesn't work bruh


