export default function Solution(input: number[]){
    input = input.filter(x=> x < 2020).sort();
    for(let i = 0; i < input.length; i++){
        for(let j = input.length-1; j > 0; j--){
            if(input[i] + input[j] === 2020){
                return input[i] * input[j];
            }
        }
    }
}
