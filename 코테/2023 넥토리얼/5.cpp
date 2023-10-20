#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);



/*
 * Complete the 'three_numbers' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER t
 *  2. INTEGER_ARRAY d
 */ 

int bt(vector<int> &d, int idx, int depth, int sum, int t){
    int ans = 0;
    if(depth == 3){
        if(sum <= t){
            return 1;
        }
    }
    for(int i=idx+1;i<d.size();i++){
        if(sum+d[i] <= t){
            ans += bt(d, i, depth+1, sum+d[i], t);
        }
    }
    return ans;
}

long three_numbers(int t, vector<int> d) {
    return bt(d, -1, 0, 0, t);
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string t_temp;
    getline(cin, t_temp);

    int t = stoi(ltrim(rtrim(t_temp)));

    string d_count_temp;
    getline(cin, d_count_temp);

    int d_count = stoi(ltrim(rtrim(d_count_temp)));

    vector<int> d(d_count);

    for (int i = 0; i < d_count; i++) {
        string d_item_temp;
        getline(cin, d_item_temp);

        int d_item = stoi(ltrim(rtrim(d_item_temp)));

        d[i] = d_item;
    }

    long result = three_numbers(t, d);

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
