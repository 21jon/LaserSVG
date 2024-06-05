import os 
import util.writer as writer
import sys

# create a wave form svg animaiton
def create_wave():
    print("Creating wave svg") 
    ani_index = 0
    for i in range(0,290,8):
        writer.write_file(f"../output/wave_{ani_index}.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" >
        <path d="M0 100 A100 {i}  0 0 1 100 100" fill="none" stroke="white" />
        <path d="M100 100 A100 {i} 0 0 0 200 100" fill="none" stroke="#ffffff" />
        </svg>""" )
        ani_index += 1
    
    for i in range(0,290, 8)[::-1]:
        writer.write_file(f"../output/wave_{ani_index}.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" >
        <path d="M0 100 A100 {i}  0 0 1 100 100" fill="none" stroke="white" />
        <path d="M100 100 A100 {i} 0 0 0 200 100" fill="none" stroke="#ffffff" />
        </svg>""" )
        ani_index += 1
    
    
    for i in range(290,0,8):
            writer.write_file(f"../output/wave_{ani_index}.svg",
            f"""<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" >
            <path d="M0 100 A100 {i}  0 0 0 100 100" fill="none" stroke="white" />
            <path d="M100 100 A100 {i} 0 0 1 200 100" fill="none" stroke="#ffffff" />
            </svg>""" )
            ani_index += 1

    
    for i in range(290,0,8)[::-1]:
            writer.write_file(f"../output/wave_{ani_index}.svg",
            f"""<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" >
            <path d="M0 100 A100 {i}  0 0 0 100 100" fill="none" stroke="white" />
            <path d="M100 100 A100 {i} 0 0 1 200 100" fill="none" stroke="#ffffff" />
            </svg>""" )
            ani_index += 1


create_wave()