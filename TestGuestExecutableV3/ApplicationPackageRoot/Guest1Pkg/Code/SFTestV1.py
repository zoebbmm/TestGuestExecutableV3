import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class TrainingModuleTest:    
    def __init__(self):
        print("start with the test SF executable")

def main(args):
    logger.info("Start to print log info.")
    print("Hello World")

if __name__ == "__main__":
	main(sys.argv)
