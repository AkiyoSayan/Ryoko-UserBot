import Ryoko
from Ryoko import app
from Ryoko import scheduler

if __name__ == '__main__':
    Ryoko.client = app

    scheduler.start()

    app.run()

