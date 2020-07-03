#include <bits/stdc++.h>

using namespace std;

//void splitString (string str, vector <string> &container)
//{
//    stringstream ss(str);
//    do {
//        string word;
//        ss >> word;
//
//        container.push_back(word);
//
//    } while (ss);
//}

void splitString (string str, vector <string> &container)
{
    vector <int> temp;
    for (unsigned int i=0; i<str.size(); i++){
        if (str[i] == ' '){
            temp.push_back(i);
        }
    }
    unsigned int head = 0;
    for (unsigned int i=0; i<temp.size(); i++){
        string ele = "";
        unsigned int tail = temp[i];
        for (unsigned int j=head; j<tail; j++){
            ele.push_back(str[j]);
        }
        container.push_back(ele);
        head = tail+1;
        if (i == temp.size()-1){
            ele = "";
            for (unsigned int k=head; k<str.size(); k++){
                ele.push_back(str[k]);
            }
            container.push_back(ele);
        }
    }
}

void splitInt (string str, vector <int> &container)
{
    vector <int> temp;
    for (unsigned int i=0; i<str.size(); i++){
        if (str[i] == ' '){
            temp.push_back(i);
        }
    }
    unsigned int head = 0;
    for (unsigned int i=0; i<temp.size(); i++){
        string ele = "";
        unsigned int tail = temp[i];
        for (unsigned int j=head; j<tail; j++){
            ele.push_back(str[j]);
        }
        container.push_back(atoi(ele.c_str()));
        head = tail+1;
        if (i == temp.size()-1){
            ele = "";
            for (unsigned int k=head; k<str.size(); k++){
                ele.push_back(str[k]);
            }
            container.push_back(atoi(ele.c_str()));
        }
    }
}

string checkString (string str)
{
    if (str.back() == ' ' || str.back() == '\n'){
        str.erase(str.end() - 1);
    }
    return str;
}

class sort_indices
{
   private:
     vector <int> mparr;
   public:
     sort_indices(vector <int> parr) : mparr(parr) {}
     bool operator()(int i, int j) const { return mparr[i]<mparr[j]; }
};

int main()
{
    // input
    int n, m, k;
    cin >> n >> m >> k;
//     n: number of people
//     m: number of bottle
//     k: amount of water per bottle

    string type;
    cin.ignore();
    getline(cin, type);
    vector <string> types;
    splitString(type, types);


    string water;
    getline(cin, water);
    water = checkString(water);
    vector <int> amount;
    splitInt(water, amount);


    // algorithm
    vector <int> indices;
    for (unsigned int i=0; i<amount.size(); i++) {
        indices.push_back(i);
    }
    sort(indices.begin(), indices.end(), sort_indices(amount));

    vector <int> bottle_number;
    int counter = types.size() - 1;
    int max_count = 0;
    int min_count = 0;
    do {
        if (types[counter] == "W") {
            while (amount[indices[indices.size()-1 - max_count]] >= k) {
                max_count++;
            }
            bottle_number.insert(bottle_number.begin(), indices[indices.size()-1 - max_count]);
            amount[indices[indices.size()-1 - max_count]] += 1;
            sort(indices.begin(), indices.end(), sort_indices(amount));
        }
        else {
            while (amount[indices[min_count]] >= k) {
                min_count++;
            }
            bottle_number.insert(bottle_number.begin(), indices[min_count]);
            amount[indices[min_count]] += 1;
            sort(indices.begin(), indices.end(), sort_indices(amount));
        }
        counter--;
    } while (counter >= 0);

    cout << "\nResult: ";
    for (int i=0; i<n; i++){
        cout << bottle_number[i] << " ";
    }

    return 0;
}
