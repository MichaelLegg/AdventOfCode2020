import { AdventDay, getInputLines } from "./common";

export default {
	part1(input: number[]): number {
		input.sort((a, b) => a - b);
		const max = input[input.length - 1] + 3;
		input.push(max);

		const adapterLookup = input.reduce((p, n) => {
			for (let i = 1; i <= 3; i++) {
				const v = n - i;
				p[v] = [...(p[v] || []), n];
			}
			return p;
		}, {} as Record<number, number[]>);

		let target = 0;
		const possible: number[] = [adapterLookup[0][0]];
		const diffs = { 1: 0, 3: 0 };
		while (possible.length) {
			const next = possible.pop()!;
			diffs[(next - target) as 1]++;
			if (adapterLookup[next]) {
				possible.push(adapterLookup[next][0]);
				target = next;
			} else {
				return diffs[1] * diffs[3];
			}
		}

		throw "result not found";
	},
	part2(input: number[]): number {
		throw "result not found";
	},
	async getInput(file: string) {
		return (await getInputLines(file, "\r\n")).map(Number);
	},
} as AdventDay<number[]>;
