import Data.List (transpose)
data Round = Round Int Int Int deriving (Show)

getFile :: IO [[String]]
getFile = map (drop 2 . words) . lines <$> readFile "d02.in"

parseGame :: [String] -> Round -> [Round]
parseGame [] round = [round]
parseGame (n : color : rest) round = 
  case last color of
    ';' -> round' (init color) : parseGame rest (Round 0 0 0)
    ',' -> parseGame rest (round' $ init color)
    _   -> parseGame rest (round' color)
    where 
      round' = parseRound round (read n)

parseRound :: Round -> Int -> String -> Round
parseRound (Round r g b) n color =
  case color of
    "red"   -> Round n g b
    "green" -> Round r n b
    "blue"  -> Round r g n

isValidRound :: Round -> Round -> Bool
isValidRound (Round r' g' b') (Round r g b)
  = (r > r') || (g > g') || (b > b')

powerGame :: [Round] -> Int
powerGame rounds = product $ maximum <$> transposed_rounds
  where
    -- Turns a list of rounds into a list of its colors and transposes it.
    transposed_rounds = transpose ((\(Round r g b) -> [r, g, b]) <$> rounds)

main :: IO ()
main = do
    games <- getFile
    let all_games = zip [1..] [parseGame game (Round 0 0 0) | game <- games]

    -- Part 1
    let valid_games = filter (any (isValidRound (Round 12 13 14)) . snd) all_games
    let count = sum $ fst <$> valid_games
    print count


    -- Part 2
    let powers = powerGame . snd <$> all_games
    let powers_sum = sum powers
    print powers_sum
