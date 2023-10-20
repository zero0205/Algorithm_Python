#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);



/*
 * Complete the 'GetMaxTime' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY initialEnergy
 *  2. LONG_INTEGER th
 */

int GetMaxTime(vector<int> initialEnergy, long th) {
    sort(initialEnergy.begin(), initialEnergy.end());   // 오름차순 정렬
    int s = 0;
    int e = int(1e9);
    int mid;
    int ans;
    long tmp = 0;
    while(s <= e){
        mid = (s+e)/2;
        tmp = 0;
        for(int i: initialEnergy){
            tmp += max(i-mid, 0);
        }
        if(tmp >= th){
            s = mid+1;
            ans = mid;
        }
        else{
            e = mid-1; 
        }
    }
    return ans;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string initialEnergy_count_temp;
    getline(cin, initialEnergy_count_temp);

    int initialEnergy_count = stoi(ltrim(rtrim(initialEnergy_count_temp)));

    vector<int> initialEnergy(initialEnergy_count);

    for (int i = 0; i < initialEnergy_count; i++) {
        string initialEnergy_item_temp;
        getline(cin, initialEnergy_item_temp);

        int initialEnergy_item = stoi(ltrim(rtrim(initialEnergy_item_temp)));

        initialEnergy[i] = initialEnergy_item;
    }

    string th_temp;
    getline(cin, th_temp);

    long th = stol(ltrim(rtrim(th_temp)));

    int result = GetMaxTime(initialEnergy, th);

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
