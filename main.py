from player import HumanPlayer, AIPlayer

def main():
    while True:
        human = HumanPlayer()
        ai = AIPlayer()

        print("\n🎮 Game Start! You vs AI\n")

        while True:
            print("\n🧍 Your Board:")
            human.board.display(reveal=True)
            print("\n🤖 Enemy Board:")
            ai.board.display(reveal=False)

            result = human.take_turn(ai.board)
            if ai.board.all_sunk():
                print("\n🎉 You win!")
                break

            result = ai.take_turn(human.board)
            if human.board.all_sunk():
                print("\n💀 AI wins!")
                break

        percent = ai.memory.get_evolution_percentage()
        print(f"\n🧠 AI has evolved by {percent}%!")
        again = input("\nPlay again with evolved AI? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()