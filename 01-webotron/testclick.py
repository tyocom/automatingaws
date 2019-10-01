import click

@click.command()
@click.option('--count',default=1, help="Number of greetings")
@click.option('--name', prompt='Your name', help="person to greet")
def hello(count, name):
    """Simple program that greets name for a total of COUNT times"""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()
