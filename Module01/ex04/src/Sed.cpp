#include "Sed.hpp"
#include <iostream>
#include <fstream>
#include <sstream>

Sed::Sed(const std::string& filename, const std::string& s1, const std::string& s2)
    : _filename(filename), _s1(s1), _s2(s2) {
}

Sed::~Sed(void) {
}

std::string Sed::_replaceOccurrences(const std::string& content) const {
    if (this->_s1.empty()) {
        return content;
    }

    std::string result;
    std::size_t startPos = 0;
    std::size_t foundPos = content.find(this->_s1, startPos);

    while (foundPos != std::string::npos) {
        // Append the segment before the match
        result.append(content, startPos, foundPos - startPos);
        // Append the replacement string
        result.append(this->_s2);
        // Advance past the matched string
        startPos = foundPos + this->_s1.length();
        foundPos = content.find(this->_s1, startPos);
    }

    // Append whatever remains after the last match
    result.append(content, startPos, content.length() - startPos);
    return result;
}

bool Sed::replace(void) const {
    if (this->_s1.empty()) {
        std::cerr << "Error: The search string s1 cannot be empty." << std::endl;
        return false;
    }

    // Open source file
    std::ifstream inFile(this->_filename.c_str());
    if (!inFile.is_open()) {
        std::cerr << "Error: Could not open file '" << this->_filename << "' for reading." << std::endl;
        return false;
    }

    // Read full content using stringstream
    std::stringstream buffer;
    buffer << inFile.rdbuf();
    std::string content = buffer.str();
    inFile.close();

    // Perform replacement without using std::string::replace
    std::string replacedContent = this->_replaceOccurrences(content);

    // Open target file
    std::string outFilename = this->_filename + ".replace";
    std::ofstream outFile(outFilename.c_str());
    if (!outFile.is_open()) {
        std::cerr << "Error: Could not create file '" << outFilename << "' for writing." << std::endl;
        return false;
    }

    outFile << replacedContent;
    outFile.close();

    return true;
}
