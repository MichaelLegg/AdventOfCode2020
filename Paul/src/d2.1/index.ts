import data from "./data";

type LineStructure = {
    from: string,
    to: string,
    character: string,
    counter: number
};

function solution(data: string[]) {
    console.log(data.reduce((a, c) => a + validatePassword(c), 0));
}

function validatePassword(line: string) {
    // lines have the format:
    // d-d c: password

    let i = 0;
    let character = "";
    let state: string = "from";

    const data: LineStructure = {
        from: "",
        to: "",
        character: "",
        counter: 0
    };

    while (i < line.length) {
        character = line[i];

        switch (state) {
            case "from":
                if(character === "-") {
                    // found -, skip one i
                    state = "to";
                } else {
                    data.from += character;
                }
                break;
            case "to":
                if(character === " ") {
                    state = "character";
                } else {
                    data.to += character;
                }
                break;
            case "character":
                // skip : and space
                state = "pwd";
                data.character = character;
                i++;
                i++;
                break;
            case "pwd":
                if (character === data.character) {
                    data.counter++;
                }
                break;
        }

        i++;
    }

    return data.counter >= Number(data.from) && data.counter <= Number(data.to) ? 1 : 0;
}

const start = process.hrtime();
solution(data);
const end = process.hrtime(start);
console.info('Execution time: %ds %dms', end[0], end[1] / 1000000);