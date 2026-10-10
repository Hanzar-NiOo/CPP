#ifndef SED_HPP
# define SED_HPP

# include <string>

class Sed {
private:
    std::string _filename;
    std::string _s1;
    std::string _s2;

    std::string _replaceOccurrences(const std::string& content) const;

public:
    Sed(const std::string& filename, const std::string& s1, const std::string& s2);
    ~Sed(void);

    bool replace(void) const;
};

#endif
