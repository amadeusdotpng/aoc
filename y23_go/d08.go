package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
    // PREP
    // ----
    input := func() []string {
        input, err := os.ReadFile("d08.in");
        if err != nil {
            panic(err)
        }
        return strings.Split(string(input), "\n")
    }();

    // split the input between the L/R instructions and the network
    instructions, mappings := input[0], input[2:len(input)-1]

    // create the network mappings
    M := make(map[string][]string)
    for _, mapping := range mappings {
        node, node_mapping := func() (string, []string) {
            mapping := strings.Split(strings.ReplaceAll(mapping, " ", ""), "=")

            node := mapping[0]
            node_mapping := strings.Split(mapping[1][1:len(mapping[1])-1], ",")

            return node, node_mapping
        }();
        M[node] = node_mapping
    }

    {
        // PART ONE
        // --------
        // follow the path using the given instructions until it hits ZZZ
        start_node := "AAA"
        idx := 0
        step := 0
        for start_node != "ZZZ" {
            nodes := M[start_node]
            direction := instructions[idx]

            switch direction {
                case 'L': start_node = nodes[0]
                case 'R': start_node = nodes[1]
            }

            idx = (idx + 1) % len(instructions)
            step += 1
        }
        fmt.Printf("Part 1: %d\n", step)
    }


    {
        // PART TWO
        // --------
        type node_step struct {loc string; step int}

        // get starting nodes
        pairs := []node_step{}
        for node := range M {
            if node[2] == 'A' { pairs = append(pairs, node_step{loc: node, step: 0}) }
        }

        // check if all of the locations are at a 'Z' node
        check := func(pairs []node_step) bool {
            for _, pair := range pairs {
                if pair.loc[2] != 'Z' { return false }
            }
            return true
        }

        // for each location, follow the path using the given instructions until it is at a 'Z' node
        i := 0
        for !check(pairs) {
            for idx := range pairs {
                pair := &pairs[idx]
                if pair.loc[2] == 'Z' { continue }

                direction := instructions[i]
                switch direction {
                    case 'L': pair.loc = M[pair.loc][0]
                    case 'R': pair.loc = M[pair.loc][1]
                }
                pair.step += 1
            }
            i = (i + 1) % len(instructions)
        }

        // basic gcd/lcm implementation
        gcd := func(a, b int) int {
            for a != b {
                if a > b { a = a - b } else { b = b - a }
            }
            return a
        }

        lcd := func(a, b int) int {
            return a * b / gcd(a, b)
        }

        // lcm of all the total steps of each location is the answer
        res := pairs[0].step
        for _, pair := range pairs {
            res = lcd(res, pair.step)
        }
        fmt.Printf("Part 2: %d\n", res)
    }
}
