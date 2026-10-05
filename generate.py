#!/usr/bin/env python3
import random

def rand_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def generate_palette(n=5):
    colors = [rand_color() for _ in range(n)]
    html = "<!DOCTYPE html><html><head><title>Palette</title></head><body style='margin:0;display:flex;height:100vh'>"
    for c in colors:
        html += f'<div style="flex:1;background:{c};display:flex;align-items:end;justify-content:center;padding:20px"><code style="color:white;text-shadow:1px 1px 2px black">{c}</code></div>'
    html += "</body></html>"
    return html

if __name__ == "__main__":
    print(generate_palette())
