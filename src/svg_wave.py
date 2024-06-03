import os 
import util.writer as writer

# create a wave form svg animaiton
def create_wave():
    ani_index = 0
    for j in range(0,2):
        for i in range(290,0):
            writer.write_file(f"../output/wave_{ani_index}.svg",
    f"""<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" >
    <path d="M0 100 A100 {i}  0 0 {1 if j == 0 else 0} 100 100" fill="none" stroke="white" />
    <path d="M100 100 A100 {i} 0 0 {j} 200 100" fill="none" stroke="#ffffff" />
</svg>""" )
            ani_index += 1
            




if __name__ == "__main__":
    create_wave()