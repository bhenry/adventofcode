(ns thirteen)

(def input "7,13,x,x,59,x,31,19")

(def input
 "13,x,x,41,x,x,x,x,x,x,x,x,x,467,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,353,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23")

(def buses (map #(Integer. %) (filter #(not (= "x" %)) (clojure.string/split input #","))))
(println buses)
(def requirements (remove #(= (second %) "x") (map-indexed #(vector %1 %2) (clojure.string/split input #","))))
(println requirements)

(def found (atom nil))

(defn meets? [ts [i b]]
  (= 0 (mod (+ ts i) (Integer. b))))

(doseq [ts (range 700404415482811 1000000000000000000000000 (Integer. (second (first requirements))))]
  (when (every? (partial meets? ts) requirements)
    (reset! found ts)
    (println ts)
    (/ 1 0)))
