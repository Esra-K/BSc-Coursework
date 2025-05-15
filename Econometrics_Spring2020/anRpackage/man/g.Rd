\name{g}
\alias{g}
\docType{data}
\title{
%%   ~~ data name/kind ... ~~
}
\description{
%%  ~~ A concise (1-5 lines) description of the dataset. ~~
}
\usage{data("g")}
\format{
  The format is:
List of 9
 $ data       :'data.frame':	325 obs. of  4 variables:
  ..$ x          : chr [1:325] "age" "wage_eur" "release_clause_eur" "overall" ...
  ..$ y          : Factor w/ 26 levels "value_eur","age",..: 1 1 1 1 1 1 1 1 1 1 ...
  ..$ coefficient: num [1:325] 0.201 0.807 0.992 0.946 0.788 ...
  ..$ label      : num [1:325] 0.2 0.8 1 0.9 0.8 0 0.4 0.2 0.2 -0.1 ...
  ..- attr(*, "na.action")= 'omit' Named int [1:351] 1 27 28 53 54 55 79 80 81 82 ...
  .. ..- attr(*, "names")= chr [1:351] "1" "27" "28" "53" ...
 $ layers     :List of 2
  ..$ :Classes 'LayerInstance', 'Layer', 'ggproto', 'gg' <ggproto object: Class LayerInstance, Layer, gg>
    aes_params: list
    compute_aesthetics: function
    compute_geom_1: function
    compute_geom_2: function
    compute_position: function
    compute_statistic: function
    data: waiver
    draw_geom: function
    finish_statistics: function
    geom: <ggproto object: Class GeomTile, GeomRect, Geom, gg>
        aesthetics: function
        default_aes: uneval
        draw_group: function
        draw_key: function
        draw_layer: function
        draw_panel: function
        extra_params: na.rm
        handle_na: function
        non_missing_aes: 
        optional_aes: 
        parameters: function
        required_aes: x y
        setup_data: function
        setup_params: function
        use_defaults: function
        super:  <ggproto object: Class GeomRect, Geom, gg>
    geom_params: list
    inherit.aes: TRUE
    layer_data: function
    map_statistic: function
    mapping: uneval
    position: <ggproto object: Class PositionIdentity, Position, gg>
        compute_layer: function
        compute_panel: function
        required_aes: 
        setup_data: function
        setup_params: function
        super:  <ggproto object: Class Position, gg>
    print: function
    setup_layer: function
    show.legend: NA
    stat: <ggproto object: Class StatIdentity, Stat, gg>
        aesthetics: function
        compute_group: function
        compute_layer: function
        compute_panel: function
        default_aes: uneval
        extra_params: na.rm
        finish_layer: function
        non_missing_aes: 
        optional_aes: 
        parameters: function
        required_aes: 
        retransform: TRUE
        setup_data: function
        setup_params: function
        super:  <ggproto object: Class Stat, gg>
    stat_params: list
    super:  <ggproto object: Class Layer, gg> 
  ..$ :Classes 'LayerInstance', 'Layer', 'ggproto', 'gg' <ggproto object: Class LayerInstance, Layer, gg>
    aes_params: list
    compute_aesthetics: function
    compute_geom_1: function
    compute_geom_2: function
    compute_position: function
    compute_statistic: function
    data: data.frame
    draw_geom: function
    finish_statistics: function
    geom: <ggproto object: Class GeomText, Geom, gg>
        aesthetics: function
        default_aes: uneval
        draw_group: function
        draw_key: function
        draw_layer: function
        draw_panel: function
        extra_params: na.rm
        handle_na: function
        non_missing_aes: 
        optional_aes: 
        parameters: function
        required_aes: x y label
        setup_data: function
        setup_params: function
        use_defaults: function
        super:  <ggproto object: Class Geom, gg>
    geom_params: list
    inherit.aes: TRUE
    layer_data: function
    map_statistic: function
    mapping: uneval
    position: <ggproto object: Class PositionIdentity, Position, gg>
        compute_layer: function
        compute_panel: function
        required_aes: 
        setup_data: function
        setup_params: function
        super:  <ggproto object: Class Position, gg>
    print: function
    setup_layer: function
    show.legend: NA
    stat: <ggproto object: Class StatIdentity, Stat, gg>
        aesthetics: function
        compute_group: function
        compute_layer: function
        compute_panel: function
        default_aes: uneval
        extra_params: na.rm
        finish_layer: function
        non_missing_aes: 
        optional_aes: 
        parameters: function
        required_aes: 
        retransform: TRUE
        setup_data: function
        setup_params: function
        super:  <ggproto object: Class Stat, gg>
    stat_params: list
    super:  <ggproto object: Class Layer, gg> 
 $ scales     :Classes 'ScalesList', 'ggproto', 'gg' <ggproto object: Class ScalesList, gg>
    add: function
    clone: function
    find: function
    get_scales: function
    has_scale: function
    input: function
    n: function
    non_position_scales: function
    scales: list
    super:  <ggproto object: Class ScalesList, gg> 
 $ mapping    :List of 2
  ..$ x: language ~x
  .. ..- attr(*, ".Environment")=<environment: 0x56085ac51148> 
  ..$ y: language ~y
  .. ..- attr(*, ".Environment")=<environment: 0x56085ac51148> 
  ..- attr(*, "class")= chr "uneval"
 $ theme      :List of 5
  ..$ legend.key      : list()
  .. ..- attr(*, "class")= chr [1:2] "element_blank" "element"
  ..$ legend.text     :List of 11
  .. ..$ family       : NULL
  .. ..$ face         : NULL
  .. ..$ colour       : NULL
  .. ..$ size         : num 9
  .. ..$ hjust        : NULL
  .. ..$ vjust        : NULL
  .. ..$ angle        : NULL
  .. ..$ lineheight   : NULL
  .. ..$ margin       : NULL
  .. ..$ debug        : NULL
  .. ..$ inherit.blank: logi FALSE
  .. ..- attr(*, "class")= chr [1:2] "element_text" "element"
  ..$ legend.title    :List of 11
  .. ..$ family       : NULL
  .. ..$ face         : NULL
  .. ..$ colour       : NULL
  .. ..$ size         : num 9
  .. ..$ hjust        : NULL
  .. ..$ vjust        : NULL
  .. ..$ angle        : NULL
  .. ..$ lineheight   : NULL
  .. ..$ margin       : NULL
  .. ..$ debug        : NULL
  .. ..$ inherit.blank: logi FALSE
  .. ..- attr(*, "class")= chr [1:2] "element_text" "element"
  ..$ legend.position : chr "right"
  ..$ panel.background: list()
  .. ..- attr(*, "class")= chr [1:2] "element_blank" "element"
  ..- attr(*, "complete")= logi FALSE
  ..- attr(*, "validate")= logi TRUE
 $ coordinates:Classes 'CoordFixed', 'CoordCartesian', 'Coord', 'ggproto', 'gg' <ggproto object: Class CoordFixed, CoordCartesian, Coord, gg>
    aspect: function
    backtransform_range: function
    clip: on
    default: FALSE
    distance: function
    expand: TRUE
    is_free: function
    is_linear: function
    labels: function
    limits: list
    modify_scales: function
    range: function
    ratio: 1
    render_axis_h: function
    render_axis_v: function
    render_bg: function
    render_fg: function
    setup_data: function
    setup_layout: function
    setup_panel_guides: function
    setup_panel_params: function
    setup_params: function
    train_panel_guides: function
    transform: function
    super:  <ggproto object: Class CoordFixed, CoordCartesian, Coord, gg> 
 $ facet      :Classes 'FacetNull', 'Facet', 'ggproto', 'gg' <ggproto object: Class FacetNull, Facet, gg>
    compute_layout: function
    draw_back: function
    draw_front: function
    draw_labels: function
    draw_panels: function
    finish_data: function
    init_scales: function
    map_data: function
    params: list
    setup_data: function
    setup_params: function
    shrink: TRUE
    train_scales: function
    vars: function
    super:  <ggproto object: Class FacetNull, Facet, gg> 
 $ plot_env   :<environment: 0x56085ac51148> 
 $ labels     :List of 4
  ..$ x    : NULL
  ..$ y    : NULL
  ..$ fill : chr "coefficient"
  ..$ label: chr "diagLabel"
 - attr(*, "class")= chr [1:2] "gg" "ggplot"
}
\details{
%%  ~~ If necessary, more details than the __description__ above ~~
}
\source{
%%  ~~ reference to a publication or URL from which the data were obtained ~~
}
\references{
%%  ~~ possibly secondary sources and usages ~~
}
\examples{
data(g)
## maybe str(g) ; plot(g) ...
}
\keyword{datasets}
