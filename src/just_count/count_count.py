import just_count.square
import click

@click.command()
@click.argument('integer')

def main(integer):
    
    print(f"The square of {integer} is {just_count.square.square(int(integer))}")

if __name__ == '__main__':
    main()