import Fs from "fs"

export default function Solution(): number{
    let numMatches = 0;
    Fs.readFileSync(`src/2/data.txt`).toString().split('\r\n').filter(x => x.length > 0).forEach(row =>
    {
        row  = row.replace("-", " ");
        row = row.replace(":", "");
        const pwArray: string[]  = row.split(" ");     

        if(+(pwArray[3][+pwArray[0]-1] === pwArray[2]) ^ +(pwArray[3][+pwArray[1]-1] === pwArray[2]))
            numMatches++;                         
    });
    return numMatches;
}