import data from "./data";

type LineStructure = {
  p1: string;
  p2: string;
  character: string;
  pwd: string;
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
    p1: "",
    p2: "",
    character: "",
    pwd: "",
  };

  while (i < line.length) {
    character = line[i];

    switch (state) {
      case "from":
        if (character === "-") {
          // found -, skip one i
          state = "to";
        } else {
          data.p1 += character;
        }
        break;
      case "to":
        if (character === " ") {
          state = "character";
        } else {
          data.p2 += character;
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
        data.pwd += character;
        break;
    }

    i++;
  }

  return (
    Number(data.pwd[Number(data.p1) - 1] === data.character) ^
    Number(data.pwd[Number(data.p2) - 1] === data.character)
  );
}

const start = process.hrtime();
solution(data);
const end = process.hrtime(start);
console.info("Execution time: %ds %dms", end[0], end[1] / 1000000);
