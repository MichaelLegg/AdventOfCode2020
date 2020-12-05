import { join } from "path";
import { promises as fs } from "fs";

export async function getInputLines(
	fileName: string,
	splitBy: string = "\r\n"
): Promise<string[]> {
	return (await fs.readFile(join(`./data/${fileName}`), "utf-8")).split(
		splitBy
	);
}

export interface AdventDay<T> {
	part1(input: T): any;
	part2(input: T): any;
	getInput(file: string): Promise<T>;
}
