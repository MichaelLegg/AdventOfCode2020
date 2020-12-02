import Chalk from "Chalk";
import Fs from "fs"
import Prompts from "Prompts";

(async () => {
    console.log(Chalk.red("Welcome to the 2020 Advent of code!"));
    
    const day = await Prompts({
        type: 'text',
        name: 'day',
        message: `${Chalk.green("To run a solution, please enter a day: ")}`
    });

    const problem = await Prompts({
        type: 'text',
        name: 'problem',
        message: `${Chalk.blue("Enter a solution number: ")}`
    })

    const answer = (await import(`./${day.day}/s${problem.problem}`)).default();

    console.log(Chalk.magenta(`The answer was: ${answer}`))
})();


 