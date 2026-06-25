import * as os from 'os';
import * as process from 'process';

// Define a type for a customizable greeting message
type GreetingMessage = {
  text: string;
  language: string;
  timestamp: Date;
  sender: string;
};

// Define an interface for a complex greeter service
interface ComplexGreeter {
  generateGreeting(recipient: string): Promise<GreetingMessage>;
  displayGreeting(greeting: GreetingMessage): void;
  logSystemInfo(): void;
}

// Implement the ComplexGreeter interface
class AdvancedGreeter implements ComplexGreeter {
  private readonly defaultLanguage: string;
  private readonly serviceName: string;
  private readonly config: {
    useUppercase: boolean;
    includeTimestamp: boolean;
    senderId: string;
  };

  constructor(language: string = 'en', serviceName: string = 'AdvancedGreeterService') {
    this.defaultLanguage = language;
    this.serviceName = serviceName;
    this.config = {
      useUppercase: Math.random() > 0.5, // Randomly decide to use uppercase
      includeTimestamp: true,
      senderId: 'SystemProcess-' + process.pid.toString(),
    };
    console.log(`[${this.serviceName}] Initialized with language: ${this.defaultLanguage}, config: ${JSON.stringify(this.config)}`);
  }

  /**
   * Asynchronously generates a customizable greeting message.
   * @param recipient The name of the person to greet.
   * @returns A Promise resolving to a GreetingMessage object.
   */
  public async generateGreeting(recipient: string): Promise<GreetingMessage> {
    return new Promise((resolve) => {
      // Simulate some asynchronous work, e.g., fetching a personalized message
      setTimeout(() => {
        let messageText: string;
        switch (this.defaultLanguage) {
          case 'es':
            messageText = `¡Hola, ${recipient}!`;
            break;
          case 'fr':
            messageText = `Bonjour, ${recipient}!`;
            break;
          default:
            messageText = `Hello, ${recipient}!`;
        }

        if (this.config.useUppercase) {
          messageText = messageText.toUpperCase();
        }

        const greeting: GreetingMessage = {
          text: messageText,
          language: this.defaultLanguage,
          timestamp: this.config.includeTimestamp ? new Date() : new Date(0), // Use Unix epoch if no timestamp
          sender: this.config.senderId,
        };
        resolve(greeting);
      }, Math.floor(Math.random() * 500) + 100); // Simulate network latency (100-600ms)
    });
  }

  /**
   * Displays the generated greeting message to the console.
   * @param greeting The GreetingMessage object to display.
   */
  public displayGreeting(greeting: GreetingMessage): void {
    const timestampStr = greeting.timestamp.getTime() !== 0 ? ` [${greeting.timestamp.toISOString()}]` : '';
    console.log(`[${this.serviceName} - ${greeting.sender}] ${greeting.text}${timestampStr} (Lang: ${greeting.language})`);
  }

  /**
   * Logs various system information for debugging and context.
   */
  public logSystemInfo(): void {
    console.log(`\n--- ${this.serviceName} System Info ---`);
    console.log(`OS Type: ${os.type()}`);
    console.log(`OS Platform: ${os.platform()}`);
    console.log(`OS Release: ${os.release()}`);
    console.log(`Architecture: ${os.arch()}`);
    console.log(`Total Memory: ${(os.totalmem() / (1024 ** 3)).toFixed(2)} GB`);
    console.log(`Free Memory: ${(os.freemem() / (1024 ** 3)).toFixed(2)} GB`);
    console.log(`CPU Cores: ${os.cpus().length}`);
    console.log(`Uptime: ${(os.uptime() / 3600).toFixed(2)} hours`);
    console.log(`Node.js Version: ${process.version}`);
    console.log(`Current Working Directory: ${process.cwd()}`);
    console.log('--- End System Info ---\n');
  }
}

// Main execution block (IIFE for encapsulation)
(async () => {
  console.log("Starting Complex Hello World Application...\n");

  const greeter = new AdvancedGreeter('pt-BR', 'MeuServicoDeSaudacaoComplexo'); // Portuguese-Brazil
  const anotherGreeter = new AdvancedGreeter('en', 'EnglishGreetingService');

  greeter.logSystemInfo();

  const recipient1 = "Mundo Complexo";
  const recipient2 = "TypeScript Dev";
  const recipient3 = "Entusiasta";

  console.log(`Generating greetings for "${recipient1}", "${recipient2}", and "${recipient3}"...`);

  // Generate greetings concurrently
  const [greeting1, greeting2, greeting3] = await Promise.all([
    greeter.generateGreeting(recipient1),
    anotherGreeter.generateGreeting(recipient2),
    greeter.generateGreeting(recipient3),
  ]);

  console("\n--- Displaying Greetings ---");
  greeter.displayGreeting(greeting1);
  anotherGreeter.displayGreeting(greeting2);
  greeter.displayGreeting(greeting3);

  // Example of a conditional greeting based on some logic
  if (new Date().getHours() < 12) {
    const morningGreeting = await greeter.generateGreeting("Bom Dia Coder");
    greeter.displayGreeting(morningGreeting);
  } else {
    const afternoonGreeting = await greeter.generateGreeting("Boa Tarde Dev");
    greeter.displayGreeting(afternoonGreeting);
  }

  console("\nApplication finished.");
})();
