(ns chargers
  (:require [clojure.string :as str]))

(def data (slurp "input.txt"))
(def adapters
  (->> (str/split-lines data)
       (map #(Integer. %))
       (sort)))

(def arrangements (atom 0))

(defn doit [input]
  (reset! arrangements 1)
  (let [connections (partition 4 1 (sort (concat [0 50000 50000 50000] input)))]
    (println connections)
    (doseq [[a b c d] connections]
      ))
  @arrangements)

(def input [
  16
  10
  15
  5
  1
  11
  7
  19
  6
  12
  4
])

(when (= (doit input) 8)
  (println "success"))
