#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);


/*
 * Complete the 'minimumMovement' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY obstacleLanes as parameter.
 */


int minimumMovement(vector<int> obstacleLanes) {
    int dp[100001][3];
    const int INF = int(1e9);
    int ans = INF;
    fill(&dp[0][0], &dp[100001][3], INF);
    int n = obstacleLanes.size();
    dp[0][1] = 0;
    for(int i=1;i<=n;i++){
        if(obstacleLanes[i-1] != 1){    // 1차선에 장애물 X
            dp[i][0] = min({dp[i-1][0], dp[i-1][1]+1, dp[i-1][2]+1});
        }
        if(obstacleLanes[i-1] != 2){
            dp[i][1] = min({dp[i-1][0]+1, dp[i-1][1], dp[i-1][2]+1});
        }
        if(obstacleLanes[i-1] != 3){
            dp[i][2] = min({dp[i-1][0]+1, dp[i-1][1]+1, dp[i-1][2]});
        }
    }
    for(int j=0;j<3;j++){
        ans = min(ans, dp[n][j]);
    }
    cout << ans << endl;
    return ans;
}
int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string obstacleLanes_count_temp;
    getline(cin, obstacleLanes_count_temp);

    int obstacleLanes_count = stoi(ltrim(rtrim(obstacleLanes_count_temp)));

    vector<int> obstacleLanes(obstacleLanes_count);

    for (int i = 0; i < obstacleLanes_count; i++) {
        string obstacleLanes_item_temp;
        getline(cin, obstacleLanes_item_temp);

        int obstacleLanes_item = stoi(ltrim(rtrim(obstacleLanes_item_temp)));

        obstacleLanes[i] = obstacleLanes_item;
    }

    int result = minimumMovement(obstacleLanes);

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
