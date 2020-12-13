(ns thirteen)

(def input "67,7,59,61")
(def input "67,x,7,59,61")
(def input "67,7,x,59,61")
(def input "1789,37,47,1889")

; (def input
;  "13,x,x,41,x,x,x,x,x,x,x,x,x,467,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,353,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23")

(def buses (map #(Integer. %) (filter #(not (= "x" %)) (clojure.string/split input #","))))
(println buses)
(def requirements (remove #(= (second %) "x") (map-indexed #(vector %1 %2) (clojure.string/split input #","))))
(println requirements)

(def found (atom nil))

(def tracker (atom 0))

(defn meets? [ts reqs]
  (every?
    (fn [[i b]]
      (= 0 (mod (+ ts i) (Integer. b))))
    reqs))

(defn gcd
      [a b]
      (if (zero? b)
      a
      (recur b, (mod a b))))

(defn lcm
      [a b]
      (/ (* a b) (gcd a b)))
;; to calculate the lcm for array
(defn lcmv [v] (reduce lcm v))

(doseq [ts (range 0 1000000000000000000000000 (Integer. (second (first requirements))))]
  (when (> ts @tracker)
    (println ts)
    (swap! tracker #(+ % 100000)))
  (when (meets? ts requirements)
    (println requirements)
    (reset! found ts)
    (println "answer " ts)
    (/ 1 0))))
