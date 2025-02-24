import time
from ban_assistant import BanAssistant

start = time.time()

ban_assistant = BanAssistant()
ban_assistant.run()

end = time.time()

print(f"\nTotal time: {round(end - start, 2)} seconds")