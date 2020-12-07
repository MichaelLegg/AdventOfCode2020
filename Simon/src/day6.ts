import { AdventDay, getInputLines } from "./common";

function part2Counted(p: number, n: string) {
	const grouped = n
		.split(/\n|/g)
		.reduce(
			(a, b) => ((a[b] = b in a ? a[b] + 1 : 1), a),
			{} as Record<string, number>
		);
	const people = n.split(/\r\n/g);
	return (
		p + Object.keys(grouped).filter((g) => grouped[g] === people.length).length
	);
}

function part2Filtered(p: number, n: string) {
	const answers = new Set([...n.replace(/\s/g, "")]);
	const people = n.split(/\r\n/g);
	return (
		p + [...answers].filter((a) => !people.find((p) => !p.includes(a))).length
	);
}

export default {
	part1(input: string[]): number {
		return input.reduce(
			(p, n) => p + new Set([...n.replace(/\s/g, "")]).size,
			0
		);
	},
	part2(input: string[], opt?: string): number {
		return input.reduce(opt === "filtered" ? part2Filtered : part2Counted, 0);
	},
	async getInput(file: string) {
		return await getInputLines(file, "\r\n\r\n");
	},
} as AdventDay<string[]>;
