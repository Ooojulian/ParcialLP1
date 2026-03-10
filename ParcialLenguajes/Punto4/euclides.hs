import System.CPUTime
import Text.Printf

mcd :: Integer -> Integer -> Integer
mcd a 0 = a
mcd a b = mcd b (a `mod` b)

-- funcion auxiliar recursiva pa simular el ciclo for de C
-- si no hago esto, haskell no va bien con la evaluacion 
cicloMcd :: Integer -> Integer -> Integer
cicloMcd 50000000 acc = acc
cicloMcd i _ = cicloMcd (i + 1) (mcd 12345678 i)

main :: IO ()
main = do
    inicio <- getCPUTime
    
    -- ejecuto las 50 millones de iteraciones
    let res = cicloMcd 1 0
    
    -- imprimo el res obligatorio pa forzar a haskell a calcular todo
    putStrLn $ "ultimo mcd calculado: " ++ show res
    
    fin <- getCPUTime
    -- getCPUTime devuelve picosegundos, toca dividir pa pasarlo a segundos
    let dif = (fromIntegral (fin - inicio)) / (10^12) :: Double
    
    printf "tiempo gastado en Haskell: %0.6f segundos\n" dif
