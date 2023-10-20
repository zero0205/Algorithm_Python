#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);



/*
 * Complete the 'getMergedLineSegments' function below.
 *
 * The function is expected to return a 2D_INTEGER_ARRAY.
 * The function accepts 2D_INTEGER_ARRAY lineSegments as parameter.
 */

vector<vector<int>> getMergedLineSegments(vector<vector<int>> lineSegments) {
    vector<vector<int>> lines;
    // lineSegments 정렬
    sort(lineSegments.begin(), lineSegments.end());
    for(auto& i:lineSegments){
        if(lines.empty()){
            lines.push_back(i);
        }
        else{
            auto& tail = lines.back();
            if(i[0] <= tail[1]){    // 같은 선분
                tail[1] = max(tail[1], i[1]);
            }
            else{
                lines.push_back(i);
            }
        }
    }
    return lines;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string lineSegments_rows_temp;
    getline(cin, lineSegments_rows_temp);

    int lineSegments_rows = stoi(ltrim(rtrim(lineSegments_rows_temp)));

    string lineSegments_columns_temp;
    getline(cin, lineSegments_columns_temp);

    int lineSegments_columns = stoi(ltrim(rtrim(lineSegments_columns_temp)));

    vector<vector<int>> lineSegments(lineSegments_rows);

    for (int i = 0; i < lineSegments_rows; i++) {
        lineSegments[i].resize(lineSegments_columns);

        string lineSegments_row_temp_temp;
        getline(cin, lineSegments_row_temp_temp);

        vector<string> lineSegments_row_temp = split(rtrim(lineSegments_row_temp_temp));

        for (int j = 0; j < lineSegments_columns; j++) {
            int lineSegments_row_item = stoi(lineSegments_row_temp[j]);

            lineSegments[i][j] = lineSegments_row_item;
        }
    }

    vector<vector<int>> result = getMergedLineSegments(lineSegments);

    for (size_t i = 0; i < result.size(); i++) {
        for (size_t j = 0; j < result[i].size(); j++) {
            fout << result[i][j];

            if (j != result[i].size() - 1) {
                fout << " ";
            }
        }

        if (i != result.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

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

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
