from dotenv import load_dotenv
import os

#simple statement to load ENV variables and print to view the output
load_dotenv()
print(os.getenv('MY_ENV'))

  