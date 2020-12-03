import Fs from "fs"

export default function Solution(): number{
    let numMatches = 0;
    Fs.readFileSync(`src/2/data.txt`).toString().split('\r\n').filter(x => x.length > 0).forEach(row =>
    {
        row  = row.replace("-", " ");
        row = row.replace(":", "");
        const pwArray: string[]  = row.split(" ");
        
        let letterCount = 0;
        for(var letter of pwArray[3])
            if(letter === pwArray[2])
                letterCount++;

        if(letterCount >= +pwArray[0] && letterCount <= +pwArray[1])
            numMatches++;
    });
    return numMatches;
}