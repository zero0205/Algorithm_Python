#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);


/*
 * Complete the 'GetMaxScore' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY scores as parameter.
 */

int GetMaxScore(vector<int> scores) {
    int n = scores.size();
    int dp[100001][2];
    // 배열 초기화
    fill(&dp[0][0], &dp[100001][2], -int(1e9));
    dp[0][0] = 0;
    dp[0][1] = 0;
    for(int i=1;i<=scores.size();i++){
        // 이번에 버림
        dp[i][0] = dp[i-1][1];
        // 이번에 안 버림
        dp[i][1] = max(dp[i-1][0], dp[i-1][1])+scores[i-1];
    }
    return max(dp[n][0], dp[n][1]);
}
int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string scores_count_temp;
    getline(cin, scores_count_temp);

    int scores_count = stoi(ltrim(rtrim(scores_count_temp)));

    vector<int> scores(scores_count);

    for (int i = 0; i < scores_count; i++) {
        string scores_item_temp;
        getline(cin, scores_item_temp);

        int scores_item = stoi(ltrim(rtrim(scores_item_temp)));

        scores[i] = scores_item;
    }

    int result = GetMaxScore(scores);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
