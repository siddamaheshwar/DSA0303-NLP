class FiniteStateAutomaton:
    def __init__(self):
        self.current_state = 0

    def transition(self, input_char):
        if self.current_state == 0:
            if input_char == 'a':
                self.current_state = 1
            else:
                self.current_state = 0
        elif self.current_state == 1:
            if input_char == 'b':
                self.current_state = 2
            else:
                self.current_state = 0
        else:
            self.current_state = 0

    def is_accepted(self):
        return self.current_state == 2

def match_ending_ab(input_string):
    automaton = FiniteStateAutomaton()
    for char in input_string:
        automaton.transition(char)
    return automaton.is_accepted()

# Input loop
while True:
    user_input = input("Enter a string (or 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        break

    if match_ending_ab(user_input):
        print(f"'{user_input}' matches the pattern.")
    else:
        print(f"'{user_input}' does not match the pattern.")
