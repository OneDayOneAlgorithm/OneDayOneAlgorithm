class Solution {
    public int solution(int a, int b, int c, int d) {
        int[] dice = new int[7];
        int[] num = {a, b, c, d};

        for (int i = 0; i < 4; i++) {
            dice[num[i]] += 1;
        }

        for (int i = 1; i < 7; i++) {
            if (dice[i] == 4) {
                return 1111 * i;
            } else if (dice[i] == 3) {
                for (int j = 1; j < 7; j++) {
                    if (dice[j] == 1) {
                        return (10 * i + j) * (10 * i + j);
                    }
                }
            } else if (dice[i] == 2) {
                for (int j = i + 1; j < 7; j++) {
                    if (dice[j] == 2) {
                        return (i + j) * Math.abs(i - j);
                    }
                }
                for (int j = 1; j < 7; j++) {
                    if (dice[j] == 1) {
                        for (int k = j + 1; k < 7; k++) {
                            if (dice[k] == 1) {
                                return j * k;
                            }
                        }
                    }
                }
            }
        }

        int min = Integer.MAX_VALUE;
        for (int i = 1; i < 7; i++) {
            if (dice[i] == 1) {
                min = Math.min(min, i);
            }
        }
        return min;
    }
}
