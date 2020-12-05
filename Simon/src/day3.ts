import { AdventDay, getInputLines } from "./common";

function traverse(map: string[], sX: number, sY: number) {
	let x = 0;
	let y = 0;
	let trees = 0;
	while (y < map.length - 1) {
		x += sX;
		y += sY;
		x = x % map[0].length;
		const c = map[y][x];
		if (c === "#") trees++;
	}
	return trees;
}

export default {
	part1(map: string[]): number {
		return traverse(map, 3, 1);
	},
	part2(map: string[]): number {
		return (
			traverse(map, 1, 1) *
			traverse(map, 3, 1) *
			traverse(map, 5, 1) *
			traverse(map, 7, 1) *
			traverse(map, 1, 2)
		);
	},
	async getInput(file: string) {
		return await getInputLines(file);
	},
} as AdventDay<string[]>;
