import Fs, { readlink } from "fs"

export default function Solution(): number{
    let input: string[] = Fs.readFileSync(`src/5/data.txt`).toString().split('\r\n').filter(x => x.length > 0);    
    const seatIds: number[] = [];

    input.forEach(currentRow => {
        const row = findCenter("F", 0, 127, currentRow.slice(0, 7))
        const column = findCenter("L", 0, 7, currentRow.slice(7, currentRow.length));
        seatIds.push((row * 8) + column);
    });
    let retval = seatIds.sort((a, b) => a - b).find(x => seatIds.find(y => y === x + 1) ? false : true);    
    return retval ? retval + 1 : 0;
}   

function findCenter(lowerChar: string, lowerBound: number, upperBound: number, characters: string): number{
    for(let i = 0; i < characters.length-1; i++){
        const newVal = (lowerBound + upperBound) / 2;
        if(characters[i] === lowerChar) upperBound =  Math.floor(newVal);
        else lowerBound = Math.ceil(newVal);
    }
    return characters[characters.length-1] === lowerChar ? lowerBound : upperBound;
}