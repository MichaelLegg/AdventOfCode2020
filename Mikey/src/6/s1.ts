import Fs from "fs"

export default function Solution(): number{
    let groups: string[] = Fs.readFileSync(`src/6/data.txt`).toString().split('\r\n\r\n').filter(x => x.length > 0);  
    let total = 0;
    groups.forEach(group => {
        const val =  [...group.replace(/\r?\n|\r/g, '')].reduce((acc, current) => acc.includes(current) ? acc : acc+current);  
        total+=val.length;         
    })
    return total;
} 