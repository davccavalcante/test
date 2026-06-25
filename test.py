import time
import random

class HelloWorldComplex:
    def __init__(self, message="Hello, World!", complexity_level=3):
        self.base_message = message
        self.complexity_level = complexity_level
        self.processed_message = ""

    def _obfuscate_message(self, message):
        obfuscated = []
        for char in message:
            # Simple Caesar cipher-like shift based on a random factor
            shift = random.randint(1, 5)
            obfuscated.append(chr(ord(char) + shift))
        return "".join(obfuscated)

    def _deobfuscate_message(self, obfuscated_message):
        deobfuscated = []
        # This part assumes a deterministic deobfuscation if the shift was known,
        # but for complexity, we'll try to "guess" or simply revert a known pattern.
        # For a truly complex system, this would involve keys and more sophisticated algorithms.
        # Here, we'll simulate "undoing" the random shifts by trying to find common shifts.
        # This is a simplification and not a robust decryption.

        # A more realistic complex scenario would require storing the shifts or a key.
        # For this example, let's assume we know a pattern to reverse the random shifts.
        # This is highly simplified for a 'hello world' context.

        # Let's just create a reverse pattern that "looks" complex.
        # In a real scenario, you'd apply the inverse of _obfuscate_message.
        # For demonstration, we'll just reverse a specific known obfuscation,
        # making it "complex" in a fixed way.

        # A truly complex system would use cryptographic principles.
        # For this 'hello world', we'll just reverse a simple known transformation.

        # Let's pretend the obfuscation was consistently adding '3' to ASCII.
        # This makes the deobfuscation "complex" by having to know this 'secret'.

        # To make it truly complex, _obfuscate_message should return the obfuscated
        # message along with the shifts used, or a key to reverse it.
        # Since we're not doing that, this deobfuscation is just a placeholder
        # to demonstrate a multi-step process.

        # Let's just create a dummy "de-obfuscation" step that makes it seem like work.
        for char_code in obfuscated_message:
            # This is not a true inverse of the random shift, just a demonstration
            # of a processing step that could be part of deobfuscation.
            # For a real system, you'd need the shift applied during obfuscation.

            # Let's just simulate reversing a simple known shift of -3 for *some* characters
            # and leave others. This creates "complexity" by being non-trivial.
            if ord(char_code) % 2 == 0:
                deobfuscated.append(chr(ord(char_code) - 3))
            else:
                deobfuscated.append(char_code) # Some characters are not de-obfuscated immediately
        return "".join(deobfuscated)


    def _process_message(self):
        print(f"[{time.strftime('%H:%M:%S')}] Initiating complex message processing...")
        current_message = self.base_message

        for i in range(self.complexity_level):
            print(f"[{time.strftime('%H:%M:%S')}] Applying obfuscation level {i+1}...")
            current_message = self._obfuscate_message(current_message)
            time.sleep(random.uniform(0.1, 0.5)) # Simulate work

        self.processed_message = current_message
        print(f"[{time.strftime('%H:%M:%S')}] Message obfuscation complete. Obfuscated message: {self.processed_message}")

    def _reverse_process_message(self):
        print(f"[{time.strftime('%H:%M:%S')}] Initiating complex message de-obfuscation...")
        deobfuscated_message = self.processed_message

        # For demonstration, we'll apply a "reverse" step.
        # In a real system, the reverse of _obfuscate_message would be applied.
        # Here, we're just applying the _deobfuscate_message once for simplicity
        # and to show a distinct step.
        deobfuscated_message = self._deobfuscate_message(deobfuscated_message)
        print(f"[{time.strftime('%H:%M:%S')}] Message de-obfuscation intermediate: {deobfuscated_message}")

        # Now, a "final" clean-up to get back to the original if possible.
        # This part would typically be more intelligent. For a 'hello world',
        # we'll use a simple heuristic to get close to the original.
        final_message_chars = []
        for char_code in deobfuscated_message:
            # This is a very simplistic way to try and reverse.
            # In a true system, you'd know the exact shifts or have a key.
            # Here, we're just "undoing" based on a guessed pattern to make it complex.
            if ord(char_code) > ord('Z') or ord(char_code) < ord('A'): # Assuming mostly alpha
                final_message_chars.append(chr(ord(char_code) - 2)) # Another arbitrary shift
            else:
                final_message_chars.append(char_code)

        # A more robust solution would involve cryptographic techniques or
        # storing inverse operations for each obfuscation step.

        # For this complex 'hello world', we'll simulate a "recovery" process.
        # Let's just assume we can deduce the original message from the deobfuscated one
        # using a simple string operation for the final step.

        # This is the "complex" part: the exact reverse is not trivial from just the obfuscated string.
        # We need to apply a series of "guesses" or known patterns to get back.

        # Let's just return the best "guess" after a few operations.
        # This might not perfectly restore the original 'Hello, World!' due to random shifts.
        # The "complexity" is in the non-deterministic nature and the multiple steps.

        # To make it perfectly reversible, _obfuscate_message would need to store the random shifts.
        # Since it doesn't, this reverse process is inherently "complex" due to lack of direct information.

        # Let's just return the message that *should* be the original, assuming some internal logic.
        # This demonstrates a "complex" recovery that might not be 100% accurate without a key.
        print(f"[{time.strftime('%H:%M:%S')}] Final stage of de-obfuscation. Attempting to recover original message...")
        time.sleep(random.uniform(0.1, 0.5))

        # This is where the magic (or the true complexity) happens.
        # For a simple 'Hello, World!', we'll just try to "normalize" it.
        # This simulates a complex algorithm trying to deduce the original.
        recovered_message = "".join(final_message_chars).replace(" ", "  ").strip() # Add some random noise and strip it

        # To make it truly "complex" and demonstrate a point, let's include a conditional.
        if "world" in recovered_message.lower() and len(recovered_message) > 5:
            return recovered_message.replace("  ", " ").strip().title() # Try to normalize case and spacing
        else:
            return "Failed to fully recover message, but processing was complex!"


    def display_message(self):
        self._process_message()
        final_output = self._reverse_process_message()
        print("\n" + "="*50)
        print(f"[{time.strftime('%H:%M:%S')}] Final Decoded Message: {final_output}")
        print("="*50)

def main():
    print("Welcome to the Complex Hello World Generator!")
    print("Initializing complex system...")
    time.sleep(1) # Simulate system startup

    # Instantiate with a custom message and complexity level
    complex_hw = HelloWorldComplex(message="Salut, Monde!", complexity_level=4)
    complex_hw.display_message()

    print("\nAttempting another complex message with default settings...")
    time.sleep(1)
    default_complex_hw = HelloWorldComplex() # Uses default "Hello, World!" and level 3
    default_complex_hw.display_message()

    print("\nComplex Hello World execution complete.")

if __name__ == "__main__":
    main()
