import random
import time
print("🏝️ Welcome to Find the Hidden Treasure!")
treasure_box=random.randint(0,9)
print("🔍🔍🔍🔍Searching for the treasure in the box...\n")
for i in range(10):
    print(f"🧰🧰🧰 Checking Box{i}...")
    time.sleep(0.5)
    if i==treasure_box:
        print(f"Hurray!Found the Treasure box {i} 🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉\n")
        break
else:
    print("Treasure not Found😢😢😢😢😢😢")
print("Game Over")