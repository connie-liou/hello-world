import random
import time

# A list of cute cat ASCII arts
cat_ascii_art = [
    r"""
     /\_/\  
    ( o.o ) 
     > ^ <
    """,
    r"""
     |\---/|
     | o_o |
      \_^_/
    """,
    r"""
      |\     /|
     (= o_o =)
      |'-'`|
     """,
    r"""
     /\     /\
    {  \'---'  }
    {  O   O  }
    ~~>  V  <~~
     \ \|/ /
      `-----'____
      /     \    \_
     {       }\  )_\_   _
     |  \_/  ) / /  \_/ /
      \__/  /(_/ /   \__/
        (__/
    """,
    r"""
       |\      _,,,---,,_
       /,`.-'`'    -.  ;-;;,_
      |,4-  ) )-,_..;\ (  `'-'
     '---''(_/--'  `-'\_)
    """,
    r"""
      _._     _,-'""`-._
     (,-.`._,'(       |\`-/|
         `-.-' \ )-`( , o o)
               `-    \`_`"'-
    """
]

# Function to display random cat ASCII art
def show_random_cat_ascii():
    print("Different cats are taking turns posing...\n")
    for i in range(5):
        time.sleep(1)  # Delay to simulate "posing"
        cat_art = random.choice(cat_ascii_art)
        print(cat_art)
        print("-" * 40)
        time.sleep(1)  # Another delay before the next cat shows up

# Let's start showing the cat ASCII art
if __name__ == "__main__":
    show_random_cat_ascii()
